import datetime
from . import scheduler
from app.energy import EnergyController


@scheduler.task(
    "interval",
    id="fetch_ev_data",
    minutes=15,
    max_instances=1,
    start_date="2000-01-01 12:19:00",
)
def fetch_ev_data():
    print("running task: Fetching EV data!")
    print(datetime.datetime.now())

    with scheduler.app.app_context():
        ec = EnergyController()
        ec.fetchEnergyData("consumption")
        print("data fetched!")
