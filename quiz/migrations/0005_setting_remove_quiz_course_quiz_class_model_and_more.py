# Generated by Django 4.0.8 on 2024-10-17 07:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0008_class_timeslot_remove_upload_course_and_more'),
        ('quiz', '0004_alter_question_figure_alter_quiz_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_order', models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question Order')),
                ('question_list', models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question List')),
                ('incorrect_questions', models.CharField(blank=True, max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Incorrect questions')),
                ('current_score', models.IntegerField(verbose_name='Current Score')),
                ('prev_score', models.IntegerField(blank=True, null=True, verbose_name='Previous Score')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete')),
                ('user_answers', models.TextField(blank=True, default='{}', verbose_name='User Answers')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('class_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.class', verbose_name='Class')),
            ],
            options={
                'permissions': (('view_settings', 'Can see completed exams.'),),
            },
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='course',
        ),
        migrations.AddField(
            model_name='quiz',
            name='class_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.class'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.TextField(choices=[('assignment', 'Assignment'), ('attend', 'Attendance'), ('mid_exam', 'Midterm Exam'), ('final_exam', 'Final Exam'), ('practice', 'Practice Quiz')]),
        ),
        migrations.DeleteModel(
            name='Sitting',
        ),
        migrations.AddField(
            model_name='setting',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz', verbose_name='Quiz'),
        ),
        migrations.AddField(
            model_name='setting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]