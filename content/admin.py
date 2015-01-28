from django.contrib import admin
from .models import Category, CategoryItem, SlideArea, Slide, Franchise, Feedback, Location


class CategoryAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ("title", "created", "active")
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("created", "updated")

	class Meta:
		model = Category


class CategoryItemAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ("title", "created", "active")
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("created", "updated")

	class Meta:
		model = CategoryItem


class SlideAreaAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ("title", "created", "active")
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("created", "updated")

	class Meta:
		model = SlideArea		


class SlideAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ("slidearea", "created", "active")
	readonly_fields = ("created", "updated")

	class Meta:
		model = Slide


class FranchiseAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ("name", "email", "city", "created", "active")
	readonly_fields = ("created", "updated")

	class Meta:
		model = Franchise


class FeedbackAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ("name", "email", "created", "active")
	readonly_fields = ("created", "updated")

	class Meta:
		model = Feedback


class LocationAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ("city", "zipcode", "active", "created")
	readonly_fields = ("created", "updated")

	class Meta:
		model = Location


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem, CategoryItemAdmin)		
admin.site.register(SlideArea, SlideAreaAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Franchise, FranchiseAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Location, LocationAdmin)