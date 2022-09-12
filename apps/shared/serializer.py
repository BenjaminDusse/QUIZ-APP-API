# from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
#
# from contacts.serializers.contact import CreateContactSerializer
# from courses.models import UserCourseSubscribe
# from group.models import UserGroupSubscribe
#
#
# class UserBaseModelSerializer(serializers.ModelSerializer):
#
#     @staticmethod
#     def get_data(given_data, user_id, author_id):
#         data = {
#             'first_name': given_data.get('first_name', ''),
#             'last_name': given_data.get('last_name', ''),
#             'middle_name': given_data.get('middle_name', ''),
#             'photo': given_data.get('photo', None),
#             'email': given_data.get('email', None),
#             'level': given_data.get('level', None),
#             'gender': given_data.get('gender', None),
#             'phones': given_data.getlist('phones', []) if given_data.get('phones') else [],
#             'users': user_id,
#         }
#         if user_id != author_id:
#             data['author'] = author_id
#         return data
#
#     def create_contact(self, user):
#         data = self.get_data(self.context['request'].data, user.id, self.context['request'].user.id)
#         serializer = CreateContactSerializer(data=data)
#         if not serializer.is_valid():
#             raise ValidationError
#         serializer.save()
#
#     def create_relations(self, user):
#         self.create_classes(self.context['request'].data, user)
#         self.create_courses(self.context['request'].data, user)
#
#     @staticmethod
#     def create_classes(data, user):
#         if data.get('classes'):
#             UserGroupSubscribe.objects.bulk_create(
#                 [UserGroupSubscribe(group_id=group, student_id=user.id) for group in data.getlist('classes')]
#             )
#
#     @staticmethod
#     def create_courses(data, user):
#         if data.get('courses'):
#             UserCourseSubscribe.objects.bulk_create(
#                 [UserCourseSubscribe(course_id=group, student_id=user.id) for group in data.getlist('courses')]
#             )
#
#     def update_relations(self, user):
#         self.delete_groups(self.context['request'].data, user)
#         self.delete_courses(self.context['request'].data, user)
#         self.create_relations(user)
#
#     @staticmethod
#     def delete_groups(data, user):
#         if data.get('deleted_classes'):
#             user.group_subscribes.filter(id=data.getlist('deleted_classes'))
#
#     @staticmethod
#     def delete_courses(data, user):
#         if data.get('deleted_courses'):
#             user.course_subscribes.filter(id=data.getlist('/home/whoami/PycharmProjects/five-skills/apps/shared/serializer.py'))
