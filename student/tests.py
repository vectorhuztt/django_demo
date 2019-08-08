from django.test import TestCase

# Create your tests here.
from student.models import Student
from django.test.client import Client


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='程参',
            sex=1,
            email='CenShen1024@sina.com',
            profession='开发',
            qq='12341231',
            phone='16610242048',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='典岩',
            sex=1,
            email='DianYan1037@sina.com',
            profession='架构',
            qq='344629813',
            phone='17764237612',
        )
        self.assertEqual(student.get_sex_display(), '男', '性别字段内容与展示的不一致！')

    def test_filter(self):
        Student.objects.create(
            name='典岩',
            sex=1,
            email='DianYan1037@sina.com',
            profession='架构',
            qq='344629813',
            phone='17764237612',
        )
        name = '典岩'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200 !')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='21312@123.com',
            profession='程序员',
            qq='213123',
            phone='13423423423',
        )
        response = client.get('/', data)
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain "test_for_post"')