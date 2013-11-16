from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
import datetime
import os


class AdamsFirstClass(object):
    def __init__(self):
        """


        """
        self.adm = "Test"
        self.user = os.getenv("USER")

    @staticmethod
    def get_time():
        """

        @return:
        """
        return datetime.datetime.now()

    def current_time(self, request):
        """

        @param request:
        @return:
        """
        time = self.get_time()
        return render_to_response("time.html", locals())

    def time_ahead(self, request, offset):
        """

        @param request:
        @param offset:
        @return:
        """
        time = self.get_time() + datetime.timedelta(hours=int(offset))
        return render_to_response("time.html", locals())