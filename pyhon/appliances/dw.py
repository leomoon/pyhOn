# pylint: disable=duplicate-code
from typing import Any, Dict

from pyhon.appliances.base import ApplianceBase


class Appliance(ApplianceBase):
    def attributes(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = super().attributes(data)
        if not self.parent.connection:
            data["parameters"]["machMode"].value = "0"
        data["active"] = bool(data.get("activity"))
        return data
