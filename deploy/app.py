from xgboost import XGBRegressor

import flask
import locale
import pandas as pd

from df_schema import df_dict

model = XGBRegressor()
model.load_model('model/best_model.json')

app = flask.Flask(__name__, template_folder='templates')


def brl(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return 'R$ {}'.format(locale.currency(value, grouping=True, symbol=False))


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('main.html')

    if flask.request.method == 'POST':
        type_ = flask.request.form['type']
        neighborhood = flask.request.form['neighborhood']

        if type_ != 'Apartamento':
            df_dict[type_] = 1.

        if neighborhood != 'Tapera':
            df_dict[neighborhood] = 1.

        df_dict['área_(m2)'] = float(flask.request.form['area'])
        df_dict['quartos'] = float(flask.request.form['bedrooms'])
        df_dict['banheiros'] = float(flask.request.form['bathrooms'])
        df_dict['vagas_de_garagem'] = float(flask.request.form['parking_spaces'])

        X = pd.DataFrame(df_dict)
        y_hat = model.predict(X)

        return flask.render_template('main.html', result=brl(y_hat[0]))


if __name__ == '__main__':
    app.run()
