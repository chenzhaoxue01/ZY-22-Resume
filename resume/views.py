from django.shortcuts import render, get_object_or_404
from .models import PersonalInfo

def resume_detail(request):
    """简历详情页面"""
    # 获取第一个个人信息记录（可以根据需要修改为特定用户）
    personal_info = get_object_or_404(PersonalInfo, pk=1)
    
    context = {
        'personal_info': personal_info,
        'educations': personal_info.educations.all(),
        'skills': personal_info.skills.all(),
        'projects': personal_info.projects.all(),
        'experiences': personal_info.experiences.all(),
    }
    
    return render(request, 'resume/resume_detail.html', context)

def home(request):
    """首页，重定向到简历详情页"""
    return resume_detail(request)