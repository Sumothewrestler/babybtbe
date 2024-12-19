from django.contrib import admin
from .models import Business, Type, Ledger, Head, Mode, Transaction

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Head)
class HeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_date', 'business', 'type', 'ledger', 
                   'head', 'amount', 'dr_or_cr', 'mode', 'gst')
    list_filter = ('transaction_date', 'business', 'type', 'ledger', 'head', 
                  'mode', 'dr_or_cr', 'gst')
    search_fields = ('business__name', 'description')
    date_hierarchy = 'transaction_date'