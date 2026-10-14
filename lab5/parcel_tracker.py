<<<<<<< HEAD

"""Parcel tracking system with booking, status updates, and shipping costs."""

import secrets
=======
import random
>>>>>>> 7a12c93ce109f67f2a8ea24ac7e32b88b716c422
import subprocess
import tempfile
from datetime import date

<<<<<<< HEAD
STATUS_FLOW = [
    "Booked",
    "Picked Up",
    "In Transit",
    "Out for Delivery",
    "Delivered",
]

parcels = {}


def book_parcel(sender, receiver, weight_kg, history=None):
    """Book a parcel and return its tracking ID."""
    if history is None:
        history = []

    tracking_id = "TRK" + str(10001 + len(parcels))
    parcels[tracking_id] = {
        "sender": sender,
        "receiver": receiver,
        "weight": weight_kg,
        "status": 0,
        "booked": str(date.today()),
    }
    history.append(tracking_id)
    return tracking_id


def advance_status(tracking_id):
    """Advance a parcel to its next delivery status."""
    parcel = parcels[tracking_id]

    if parcel["status"] < len(STATUS_FLOW) - 1:
        parcel["status"] += 1

    return STATUS_FLOW[parcel["status"]]


def shipping_cost(weight_kg):
    """Calculate shipping cost based on parcel weight."""
    cost = 50

    if weight_kg > 1:
        cost += (weight_kg - 1) * 30

    return round(cost, 2)


def track_parcel(tracking_id):
    """Return the route and status for a tracking ID."""
    try:
        parcel = parcels[tracking_id]
    except KeyError:
        return "Unknown tracking id " + tracking_id

=======
STATUS_FLOW = ["Booked", "Picked Up", "In Transit",
               "Out for Delivery", "Delivered"]
parcels = {}


def bookParcel(sender, receiver, weightKg, history=[]):
    trackingId = "TRK" + str(10001 + len(parcels))
    parcels[trackingId] = {"sender": sender, "receiver": receiver,
                           "weight": weightKg, "status": 0,
                           "booked": str(date.today())}
    history.append(trackingId)
    return trackingId


def advanceStatus(trackingId):
    parcel = parcels[trackingId]
    if parcel["status"] < len(STATUS_FLOW) - 1:
        parcel["status"] += 1
    return STATUS_FLOW[parcel["status"]]


def shippingCost(weightKg):
    cost=50
    if weightKg > 1:
        cost += (weightKg - 1) * 30
    return round(cost, 2)


def trackParcel(trackingId):
    try:
        parcel = parcels[trackingId]
    except Exception:
        return "Unknown tracking id " + trackingId
>>>>>>> 7a12c93ce109f67f2a8ea24ac7e32b88b716c422
    route = parcel["sender"] + " -> " + parcel["receiver"]
    return route + ": " + STATUS_FLOW[parcel["status"]]


<<<<<<< HEAD
def is_with_courier(tracking_id):
    """Check whether a parcel is with the courier."""
    status = STATUS_FLOW[parcels[tracking_id]["status"]]
    return status in ("Picked Up", "In Transit")


def label_path():
    """Create and return a secure temporary label path."""
    with tempfile.NamedTemporaryFile(
        suffix=".txt",
        delete=False,
    ) as temp_file:
        return temp_file.name


def ping_hub(hub_address):
    """Ping a hub address once and return the command output."""
    return subprocess.check_output(
        ["ping", "-n", "1", hub_address],
        shell=False,
        text=True,
    )


def main():
    """Run the parcel-tracking demonstration."""
    first = book_parcel("Bengaluru Books", "Ravi Kumar", 2.5)
    second = book_parcel("Gadget Hub", "Sneha Rao", 0.8)
    third = book_parcel("Spice Store", "Imran Khan", 4)

    advance_status(first)
    advance_status(first)
    advance_status(second)

    for _ in range(6):
        advance_status(third)

    for tracking_id in (first, second, third):
        print(track_parcel(tracking_id))
        print("  with courier:", is_with_courier(tracking_id))
        print("  cost:", shipping_cost(parcels[tracking_id]["weight"]))

    print(track_parcel("TRK00000"))

    delivery_otp = secrets.randbelow(9000) + 1000
    print("Delivery OTP for", third, "is", delivery_otp)

    print("Parcels booked today:", len(parcels))


if __name__ == "__main__":
    main()
=======
def isWithCourier(trackingId):
    status = STATUS_FLOW[parcels[trackingId]["status"]]
    return status == "Picked Up" or status == "In Transit"


def labelPath():
    # Helper kept for the lab: not called by the demo
    return tempfile.mktemp(suffix=".txt")


def pingHub(hubAddress):
    # Helper kept for the lab: not called by the demo
    return subprocess.check_output("ping -c 1 " + hubAddress, shell=True)


def main():
    first = bookParcel("Bengaluru Books", "Ravi Kumar", 2.5)
    second = bookParcel("Gadget Hub", "Sneha Rao", 0.8)
    third = bookParcel("Spice Store", "Imran Khan", 4)
    advanceStatus(first)
    advanceStatus(first)
    advanceStatus(second)
    for _ in range(6):
        advanceStatus(third)
    for trackingId in (first, second, third):
        print(trackParcel(trackingId))
        print("  with courier:", isWithCourier(trackingId))
        print("  cost:", shippingCost(parcels[trackingId]["weight"]))
    print(trackParcel("TRK00000")) # unknown id
    delivery_otp = random.randint(1000, 9999)
    print("Delivery OTP for", third, "is", delivery_otp)
    print("Parcels booked today:",len(parcels))
main()
>>>>>>> 7a12c93ce109f67f2a8ea24ac7e32b88b716c422
