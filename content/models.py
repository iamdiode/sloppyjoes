from django.db import models


class Category(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "categories"
		unique_together = ("title", "slug")
		ordering = ["created"]


class CategoryItem(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='items')
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug")
		ordering = ["created"]


class SlideArea(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug")
		ordering = ["created"]


class Slide(models.Model):
	slidearea = models.ForeignKey(SlideArea)
	image = models.ImageField(upload_to='slides')
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.slidearea.title

	class Meta:
		ordering = ["created"]


class Franchise(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	mobile = models.CharField(max_length=12)
	address = models.TextField()
	city = models.CharField(max_length=120)
	comments = models.TextField()
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["created"]


class Feedback(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	subject = models.CharField(max_length=120)
	message = models.TextField()
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["created"]		


class Location(models.Model):
	address = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=120)
	zipcode = models.CharField(max_length=12, blank=True, null=True)
	country = models.CharField(max_length=120, default='India')
	active = models.BooleanField(default='active')
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.city

	class Meta:
		ordering = ["city"]