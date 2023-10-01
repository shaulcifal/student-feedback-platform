from django.urls import path


from .views import (
    renderFeedbackSubmit,
    renderFeedbackView,
    renderFacultyFeedbackView,
    renderEditDraftView,
    renderError,
    # TestView,
)

urlpatterns = [
    path('submit-feedback', renderFeedbackSubmit, name='submit-feedback'),
    path('view-feedback', renderFeedbackView, name='view-feedback'),
    path('view-feedback-faculty', renderFacultyFeedbackView, name='view-feedback-faculty'),
    path('edit-draft/<str:draft_id>', renderEditDraftView, name='edit-draft'),
    # path('test', TestView, name='test'),
    path('feedback-error', renderError, name='feedback-error'),
]