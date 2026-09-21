from django.contrib import admin

from checkins.models import MoodEntry

# admin.site.register(MoodEntry)


# Lines below will show score, column and creation time in table of admin
# In the search bar you'll see you can find reason by searching key word on reasons.
@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = (
        "score",
        "energy_level",
        "created_at",
    )  # If I remove one of the column, you'll get columns without deleted one.
    search_fields = ("reason",)
    list_filter = ("score",)


# Serach_field is usefull if you're going to search by keywords and limit the results.
# list_display is usefull if you want to see the database more neater and see items by columns that you'll define.

# list_filter will help you to filter and limit items by their score. And maybe 3 people got 10 score than you can see in in filter bar.

# In search field you should write a keywords of reason e.g, but in filter you can see all the scores and it's Items.
# Filter is usefull for creation time, score and some fields that are limited.
