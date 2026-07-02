from typing import Dict, List


class PayloadStorageService:

    def __init__(self):

        self._payloads: List[Dict] = []

    def save_payload(
            self,
            payload: Dict):

        self._payloads.append(
            payload
        )

    def get_latest_payload(self):

        if not self._payloads:
            return None

        return self._payloads[-1]

    def get_all_payloads(self):

        return self._payloads

    def get_count(self):

        return len(
            self._payloads
        )


payload_storage_service = (
    PayloadStorageService()
)