# serializers.py
from rest_framework import serializers
from api_lycs_fid.models import LoyaltyProgram, LoyaltyTier

class LoyaltyTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyTier
        fields = ['id','montant', 'equiPoints']

class LoyaltyProgramSerializer(serializers.ModelSerializer):
    tiers = LoyaltyTierSerializer(many=True)

    class Meta:
        model = LoyaltyProgram
        fields = ['user', 'tiers']

    def create(self, validated_data):
        tiers_data = validated_data.pop('tiers')
        program = LoyaltyProgram.objects.create(**validated_data)
        for tier_data in tiers_data:
            LoyaltyTier.objects.create(program=program, **tier_data)
        return program

    def update(self, instance, validated_data):
        tiers_data = validated_data.pop('tiers', [])
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        # Supprimer les paliers existants et les recréer
        instance.tiers.all().delete()
        for tier_data in tiers_data:
            LoyaltyTier.objects.create(program=instance, **tier_data)

        return instance
