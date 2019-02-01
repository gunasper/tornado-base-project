from .base import BaseHandler, request_counter

class StatusHandler(BaseHandler):
    """
    Handler implementing GET method to require server status information
    """
    @request_counter
    async def get(self):
        """
        GETs information about server status
        """
        response = {}
        response["up_time_sec"] = self.application.up_time
        response["up_time_iso"] = self.application.up_time_iso
        response["total_requests"] = self.application.request_counter
        self.write(response)
