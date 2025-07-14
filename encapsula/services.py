from .models import Customer


class CustomerService:
    @staticmethod
    def create_customer(name, phone, email=None, address=None):
        customer = Customer(name=name, phone=phone, email=email, address=address)
        customer._allow_save = True
        customer.save()
        return customer


#
# class CustomerService:
#     # @staticmethod
#     # def create_customer(name, phone, email=None, address=None):
#     #     customer = Customer(name=name, phone=phone, email=email, address=address)
#     #     customer.save()
#     #     return customer
#
#     @staticmethod
#     def create_customer(name, phone, email=None, address=None):
#         try:
#             customer = Customer(name=name, phone=phone, email=email, address=address)
#             customer.save()
#             return customer
#         except Exception as e:
#             # log the error here
#             raise Exception(f"Customer yaratishda xatolik: {str(e)}")
#
#
#     @staticmethod
#     def update_customer(customer, **data):
#         model_fields = [field.name for field in customer._meta.get_fields()]
#         for field, value in data.items():
#             if field in model_fields:
#                 setattr(customer, field, value)
#         customer.save()
#         return customer
#
#
#     # @staticmethod
#     # def update_customer(customer, **data):
#     #     for field, value in data.items():
#     #         if hasattr(customer, field):
#     #             setattr(customer, field, value)
#     #     customer.save()
#     #     return customer
