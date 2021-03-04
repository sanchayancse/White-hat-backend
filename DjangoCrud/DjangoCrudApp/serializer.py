class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = "__all__"