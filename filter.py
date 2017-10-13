from data_transfer import get_all_img_vectors, txt_to_list
import plotly_auth
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

if __name__ == "__main__":
    plotly_auth.AUTH()
    ls = txt_to_list()
    # img = get_all_img_vectors()

    total = []
    for i in range(10):
        total.append(0)
    for vector in ls:
        ring = vector[3]
        ring = int(int(ring) / 10)
        total[ring] += 1

    data = [go.Bar(
                x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                y = total
    )]

    py.plot(data, filename='basic-bar')
