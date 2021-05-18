from app.energy.dao import EnergyDAO

class EnergyController:
    def __init__(self):
        self.energyDAO = EnergyDAO()
        pass

    def getConsumptionData(self, hours):
        data = self.energyDAO.fetchConsumptionData(hours)
        return data

    def fetchConsumptionData(self):
        data = self.energyDAO.fetchData('consumption')
        self.energyDAO.insertData('consumption', data)

    def fetchProductionData(self):
        data = self.energyDAO.fetchData('production')
        self.energyDAO.insertData('production', data)
