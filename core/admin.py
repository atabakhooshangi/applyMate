from django.contrib import admin
import vercel_blob
from .models import Application

import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = Path(f"{BASE_DIR}/.env")
load_dotenv(dotenv_path=env_path)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'level', 'country', 'type', 'feedback']
    list_filter = ['level', 'country', 'type', 'feedback']
    search_fields = ['company', 'position', 'country', 'type', 'feedback']

    # def save_model(self, request, obj, form, change):
    #     # s = super().save_model(request, obj, form, change)
    #     if obj.company_logo_uri is None:
    #         logo_file = obj.company_logo
    #         logo_file.seek(0)
    #         logo_uri = vercel_blob.put(f"{obj.file_name_prefix}_logo_{obj.id}", logo_file.read(), {})
    #         obj.company_logo_uri = logo_uri['url']
    #         logo_file.close()
    #     if obj.description_image_uri is None:
    #         descr_file = obj.description_image
    #         descr_file.seek(0)
    #         descr_uri = vercel_blob.put(f"{obj.file_name_prefix}_descr_{obj.id}", descr_file.read(), {})
    #         descr_file.close()
    #         obj.description_image_uri = descr_uri['url']
    #     obj.description_image = None
    #     obj.company_logo = None
    #     obj.save()
    #     return


admin.site.register(Application, ApplicationAdmin)
