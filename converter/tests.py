from django.test import TestCase


# Create your tests here.
class RouteTemplateTester(TestCase):

    def route(self, path, template_name):
        self.path = path
        self.template_name = template_name
        response = self.client.get(self.path)
        self.assertTemplateUsed(response, self.template_name)


class HomePageTest(RouteTemplateTester):

    def test_home_page_returns_template(self):

        self.route('/pdf_converter/', 'home.html')
