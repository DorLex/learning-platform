from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import F, FilteredRelation, Q, QuerySet
from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnList

from courses.models import CourseAccess
from courses.serializers.access import CourseAccessSerializer
from courses.serializers.lesson import LessonWithInfoByCourseSerializer
from lessons.models import Lesson

User: type[AbstractBaseUser] = get_user_model()


class CourseService:
    def get_courses_accesses(self) -> ReturnList:
        courses_accesses: QuerySet[CourseAccess] = CourseAccess.objects.all()
        serializer: CourseAccessSerializer = CourseAccessSerializer(courses_accesses, many=True)
        return serializer.data

    def get_course_lessons_by_user(self, course_id: int, user: User) -> ReturnList:
        course_accesses: QuerySet[CourseAccess] = self.get_course_accesses_by_user(user)

        access_course_id: int = get_object_or_404(
            course_accesses.values_list('course_id', flat=True),
            course_id=course_id,
        )

        lesson_with_info: QuerySet[Lesson, dict] = (
            Lesson.objects.filter(
                courses__id=access_course_id,
            )
            .values('title')
            .alias(
                view_info=FilteredRelation(
                    'views',
                    condition=Q(views__user=user),
                ),
            )
            .annotate(
                viewing_status=F('view_info__viewing_status'),
                viewing_time=F('view_info__viewing_time'),
                last_viewing_time=F('view_info__last_viewing_time'),
            )
        )

        serializer: LessonWithInfoByCourseSerializer = LessonWithInfoByCourseSerializer(lesson_with_info, many=True)
        return serializer.data

    def get_course_accesses_by_user(self, user: User) -> QuerySet[CourseAccess]:
        return CourseAccess.objects.filter(user=user, is_valid=True)
