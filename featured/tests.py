from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase
from django.core.urlresolvers import reverse

from featured.models import Featured, Category, get_featured_queryset_for


class FeaturedModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Joe')
        self.user2 = User.objects.create(username='Doe')
        self.category = Category.objects.create(slug='category', active=True)
        self.category2 = Category.objects.create(slug='category2', active=True)

    def test_create_without_category(self):
        self.assertRaises(IntegrityError, Featured.objects.create, content_object=self.user)
    
    def test_create(self):
        featured = Featured.objects.create(content_object=self.user, category=self.category)
        self.assertIsInstance(featured, Featured)
        self.assertEqual(featured.content_object, self.user)

    def test_generic_queryset(self):
        featured = Featured.objects.create(content_object=self.user, category=self.category)
        featured = Featured.objects.create(content_object=self.user2, category=self.category2)

        manager = get_featured_queryset_for(User)

        self.assertEqual(list(manager.all().order_by('pk')), [self.user, self.user2])

    def test_generic_queryset_for_category(self):
        featured = Featured.objects.create(content_object=self.user, category=self.category)
        featured = Featured.objects.create(content_object=self.user2, category=self.category2)

        manager = get_featured_queryset_for(User, category=self.category)

        self.assertEqual(list(manager.all()), [self.user])


class CategoryModelTest(TestCase):
    def test_create(self):
        category = Category.objects.create(slug='category')

        self.assertIsInstance(category, Category)
        self.assertIsNotNone(category.pk)
        self.assertFalse(category.active)

    def test_create_same_slug(self):
        Category.objects.create(slug='category')
        
        category = Category(slug='category')
        self.assertRaises(IntegrityError, category.save)

    def test_create_active_true(self):
        category = Category.objects.create(slug='category', active=True)

        self.assertTrue(category.active)


class CategoryFeaturedTest(object):
    def setUp(self):
        self.category = Category.objects.create(slug='category')
        self.user1 = User.objects.create(username='joe1')
        self.user2= User.objects.create(username='joe2')
        self.user3 = User.objects.create(username='joe3')
        Featured.objects.create(content_object=self.user1, category=self.category)
        Featured.objects.create(content_object=self.user2, category=self.category)
        self.url = reverse('featured_category_list', kwargs={'slug': self.category.slug, 'model': 'auth.user'})

    def test_get_inactive(self):
        response = self.client.get(self.url)

        self.assertEqual(404, response.status_code)

    def test_get_active(self):
        self.category.active = True
        self.category.save()
        manager = get_featured_queryset_for(User, category=self.category)

        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(list(manager.all()), list(response.context['object_list'].all()))
        self.assertTemplateUsed(response, 'featured/featured_list.html')
