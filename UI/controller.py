import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._view._txt_result.controls.clear()
        self._model.clearG()

        try:
            dist_min=int(self._view._txtIn.value)
            self._model.creaGrafo(dist_min)
            self._view._txt_result.controls.append(ft.Text(f"Il numero di nodi è: {self._model.getNNodes()}"))
            self._view._txt_result.controls.append(ft.Text(f"Il numero di archi è: {self._model.getNEdges()}"))
            listaArchi=self._model.allEdges()
            for arco in listaArchi:
                air1 = arco[0].id
                air2 = arco[1].id
                weight = arco[2]
                self._view._txt_result.controls.append(ft.Text(f"{air1} e {air2}, distanza media: {weight}"))




        except ValueError:
            self._view._txt_result.controls.append(ft.Text("Inserire un valore valido"))
        self._view.update_page()

        pass

