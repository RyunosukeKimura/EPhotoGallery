from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    # 写真投稿ページのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),

    # 編集ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo-edit/<int:pk>',
         views.PhotoEditView.as_view(),
         name = 'photo_edit'
         ),

    # 投稿完了ページのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),

    # カテゴリ一覧ページ
    # photo/<Categorys テーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name = 'photos_cat'),
    
    # ユーザー投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'),

    # 詳細ページ
    # photo-detail/<Photo post テーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo_detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail'),
     
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    # 投稿写真の削除
    # photo/<Photo postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name = 'photo_delete'),
]