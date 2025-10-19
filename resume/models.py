from django.db import models

class PersonalInfo(models.Model):
    """个人信息模型"""
    name = models.CharField(max_length=100, verbose_name='姓名')
    student_id = models.CharField(max_length=20, verbose_name='学号')
    major = models.CharField(max_length=100, verbose_name='专业')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=20, verbose_name='电话')
    address = models.CharField(max_length=200, verbose_name='地址', blank=True)
    photo = models.ImageField(upload_to='photos/', verbose_name='照片', blank=True)
    introduction = models.TextField(verbose_name='个人简介', blank=True)
    
    class Meta:
        verbose_name = '个人信息'
        verbose_name_plural = '个人信息'
    
    def __str__(self):
        return self.name

class Education(models.Model):
    """教育背景模型"""
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='educations')
    school = models.CharField(max_length=100, verbose_name='学校')
    degree = models.CharField(max_length=50, verbose_name='学位')
    major = models.CharField(max_length=100, verbose_name='专业')
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期', null=True, blank=True)
    description = models.TextField(verbose_name='描述', blank=True)
    
    class Meta:
        verbose_name = '教育背景'
        verbose_name_plural = '教育背景'
    
    def __str__(self):
        return f"{self.school} - {self.degree}"

class Skill(models.Model):
    """技能模型"""
    SKILL_LEVELS = [
        ('beginner', '初级'),
        ('intermediate', '中级'),
        ('advanced', '高级'),
        ('expert', '专家'),
    ]
    
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100, verbose_name='技能名称')
    level = models.CharField(max_length=20, choices=SKILL_LEVELS, verbose_name='技能水平')
    description = models.TextField(verbose_name='描述', blank=True)
    
    class Meta:
        verbose_name = '技能'
        verbose_name_plural = '技能'
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

class Project(models.Model):
    """项目经验模型"""
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200, verbose_name='项目名称')
    role = models.CharField(max_length=100, verbose_name='担任角色')
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期', null=True, blank=True)
    description = models.TextField(verbose_name='项目描述')
    technologies = models.CharField(max_length=200, verbose_name='使用技术')
    link = models.URLField(verbose_name='项目链接', blank=True)
    
    class Meta:
        verbose_name = '项目经验'
        verbose_name_plural = '项目经验'
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    """工作经验模型"""
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=100, verbose_name='公司名称')
    position = models.CharField(max_length=100, verbose_name='职位')
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期', null=True, blank=True)
    description = models.TextField(verbose_name='工作描述', blank=True)
    
    class Meta:
        verbose_name = '工作经验'
        verbose_name_plural = '工作经验'
    
    def __str__(self):
        return f"{self.company} - {self.position}"