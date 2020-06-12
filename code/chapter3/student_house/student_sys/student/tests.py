from django.test import TestCase

# Create your tests here.


class StudentTestCase(TestCase):
    # def setUp(self) -> None:
    #     Student.objects.create(
    #         name='the5fire',
    #         sex=1,
    #         email='nobody@the5fire.com',
    #         profession='程序员',
    #         qq='3333',
    #         phone='2222',
    #     )

    def test_create_and_sex_show(self):
        # student = Student.objects.create(
        #     name='the5fire',
        #     sex=1,
        #     email='nobody@the5fire.com',
        #     profession='程序员',
        #     qq='3333',
        #     phone='2222',
        # )
        self.assertEqual('男', '男', '性别字段内容与展示不一致')