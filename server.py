from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField, Label, ValidationError

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ldjflkjdaf_lkjadlfkj_akldjflkjaflkjadljf'


def type_error(form, width):
    if not width.data.isdigit():
        raise ValidationError(f"Ширина должна быть целым числом")

def type_error_1(form, length):
    if not length.data.isdigit():
        raise ValidationError(f"Длина должна быть целым числом")


class TestForm(FlaskForm):
    width = StringField('Ширина в см', validators=[DataRequired(message='Введите ширину'), type_error])
    length = StringField('Длина в см', validators=[DataRequired(message='Введите длину'), type_error_1])
    measure_answer = RadioField(
        'Вы честно измеряли?',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    lang_answer = RadioField(
        'На иврите говорите?',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    submit = SubmitField('Узнать результат')

    def type_error(self, width):
        print('dsada')
        raise ValidationError(f"Длина должна быть целым числом")


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm()
    if form.validate_on_submit():
        return render_template(
            'result.html',
            measure=form.measure_answer.data,
            lang=form.lang_answer.data,
            ci=(int(form.width.data) / int(form.length.data)) * 100
        )
    return render_template('test.html', form=form)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
