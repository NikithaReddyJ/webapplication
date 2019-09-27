from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns=[

        url(r'^$', views.app1view, name="views"),
        url(r'^dashboard/$', views.dashboardview, name="dashboard"),
        url(r'^newframe/$', views.newframeview, name="newframe"),
        url(r'^T/$', views.Tview, name="T"),
        url(r'^table/ftable/$', views.ftableview, name="ftable"),
        url(r'^table1/ftable1/$', views.ftable1view, name="ftable1"),
        url(r'^table2/ftable2/$', views.ftable2view, name="ftable2"),
        url(r'^deleteview/(?P<k_id>\w+)/$',views.deleteview, name="xyz"),
        url(r'^updateview/(?P<m_id>\w+)/$',views.update, name="xy"),
        url(r'^update/(?P<m_id>\w+)/$',views.updateview, name="x"),
        url(r'^userview/$',views.userview, name="fuserview"),





        url(r'^userprofile/$', views.userprofileview, name="userprofile"),
        url(r'^profile/', TemplateView.as_view(template_name="profile.html"), name='profile'),
        url(r'^user/', TemplateView.as_view(template_name="user.html"), name='user'),
        url(r'^land/', TemplateView.as_view(template_name="land.html"),name='land'),
        url(r'^d1/', TemplateView.as_view(template_name="d1.html"),name='d1'),
        url(r'^d2/', TemplateView.as_view(template_name="d2.html"),name='d2'),
        url(r'^top/', TemplateView.as_view(template_name="top.html"),name='top'),
        url(r'^top1/', TemplateView.as_view(template_name="top1.html"),name='top1'),
        url(r'^top2/', TemplateView.as_view(template_name="top2.html"),name='top2'),
        url(r'^table/', TemplateView.as_view(template_name="table.html"), name='table'),
        url(r'^table1/', TemplateView.as_view(template_name="table1.html"), name='table1'),
        url(r'^table2/', TemplateView.as_view(template_name="table2.html"), name='table2'),
        url(r'^T0/', TemplateView.as_view(template_name="T0.html"), name='T0'),
        url(r'^T1/', TemplateView.as_view(template_name="T1.html"), name='T1'),
        url(r'^T2/', TemplateView.as_view(template_name="T2.html"), name='T2'),
        url(r'^TD1/', TemplateView.as_view(template_name="TD1.html"), name='TD1'),
        url(r'^TD2/', TemplateView.as_view(template_name="TD2.html"), name='TD2'),
        url(r'^du1/', TemplateView.as_view(template_name="du1.html"),name='du1'),
        url(r'^du2/', TemplateView.as_view(template_name="du2.html"),name='du2'),
        url(r'^du3/', TemplateView.as_view(template_name="du3.html"),name='du3'),
        url(r'^du4/', TemplateView.as_view(template_name="du4.html"),name='du4'),
        url(r'^line/', TemplateView.as_view(template_name="line.html"),name='line'),
        url(r'^line1/', TemplateView.as_view(template_name="line1.html"),name='line1'),
        url(r'^vertical/', TemplateView.as_view(template_name="vertical.html"),name='vertical'),


]
