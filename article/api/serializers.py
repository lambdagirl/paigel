from rest_framework import serializers
from ..models import Article, Images

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields=['id','title','slug','body','modified','pub_date']
        

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields=['article','image']

