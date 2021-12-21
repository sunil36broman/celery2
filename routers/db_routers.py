class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'main','django_celery_beat','django_celery_results'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'report_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'report_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'report_db'
        return None

class DhamRouter:
    route_app_labelss = {'dham'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labelss:
            return 'dham_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labelss:
            return 'dham_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labelss or
            obj2._meta.app_label in self.route_app_labelss
        ):
           return True
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print("db---------------",db == 'dham_db')
        if app_label in self.route_app_labelss:
            return db == 'dham_db'
        return None        




# class Blog:
#     route_app_labels = {'blog'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'blog_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'blog_db'
#         return None

#     # def allow_relation(self, obj1, obj2, **hints):
#     #     if (
#     #         obj1._meta.app_label in self.route_app_labels or
#     #         obj2._meta.app_label in self.route_app_labels
#     #     ):
#     #        return True
#     #     return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'blog_db'
#         return None     


# class Books:
#     route_app_labelss = {'books'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labelss:
#             return 'books_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labelss:
#             return 'books_db'
#         return None

#     # def allow_relation(self, obj1, obj2, **hints):
#     #     if (
#     #         obj1._meta.app_label in self.route_app_labels or
#     #         obj2._meta.app_label in self.route_app_labels
#     #     ):
#     #        return True
#     #     return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labelss:
#             return db == 'books_db'
#         return None  

# class DFS:
#     route_app_labelss = {'dfs'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labelss:
#             return 'dfs_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labelss:
#             return 'dfs_db'
#         return None

#     # def allow_relation(self, obj1, obj2, **hints):
#     #     if (
#     #         obj1._meta.app_label in self.route_app_labels or
#     #         obj2._meta.app_label in self.route_app_labels
#     #     ):
#     #        return True
#     #     return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labelss:
#             return db == 'dfs_db'
#         return None                      