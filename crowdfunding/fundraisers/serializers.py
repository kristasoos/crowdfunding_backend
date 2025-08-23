from rest_framework import serializers
from django.apps import apps
 
class FundraiserSerializer(serializers.ModelSerializer):
    # we set the owner to be read only due to not being able to create project on behalf of other people
    owner=serializers.ReadOnlyField(source='owner.id')
   
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter=serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model=apps.get_model('fundraisers.PLedge')
        fields='__all__'

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges=PledgeSerializer(many=True, read_only=True)

