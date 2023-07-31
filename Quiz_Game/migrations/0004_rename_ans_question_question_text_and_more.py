# Generated by Django 4.2.3 on 2023-07-29 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Quiz_Game", "0003_question_delete_quiz"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="ans",
            new_name="question_text",
        ),
        migrations.RemoveField(
            model_name="question",
            name="op1",
        ),
        migrations.RemoveField(
            model_name="question",
            name="op2",
        ),
        migrations.RemoveField(
            model_name="question",
            name="op3",
        ),
        migrations.RemoveField(
            model_name="question",
            name="op4",
        ),
        migrations.RemoveField(
            model_name="question",
            name="question",
        ),
        migrations.CreateModel(
            name="Choice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("choice_text", models.CharField(max_length=200)),
                ("ans", models.CharField(max_length=200)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Quiz_Game.question",
                    ),
                ),
            ],
        ),
    ]