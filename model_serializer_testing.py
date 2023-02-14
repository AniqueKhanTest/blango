from rest_framework import serializers
from blog.models import Post
from django.utils.text import slugify


class PostSerializer(serializers.ModelSerializer):
    # This is just for experimenting with serializers , this does not apply to Blango
    slug = serializers.SlugField(required=False)
    autogenerate_slug = serializers.BooleanField(required=False, write_only=True, default=False)

    class Meta:
        model = Post

        # fields = "__all__"
        exclude = ["modified_at", "created_at"]

    def validate(self, data):
        if not data.get("slug"):
            if data['autogenerate_slug']:
                data['slug'] = slugify(data['title'])
            else:
                raise serializers.ValidationError("slug is required if autogenerate slug is not set.")

        del data['autogenerate_slug']
        return data
