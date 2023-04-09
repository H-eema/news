from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase


class SignupPageTests(TestCase):
    def test_url_at_location(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_name_and_tempalte(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
    
    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'testuser',
                'email': 'testuser@test.com',
                'password1': 'testpass123',
                'password2': 'testpass123',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@test.com')