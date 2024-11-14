from django.db import models



class Visit(models.Model):
    """
    The Visit model logs individual visits with a timestamp.
    Stores the date and time of each visit.
    auto_now_add=True sets the timestamp when the Visit instance is created, and it does not update on further saves.
    """
    timestamp = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"Visit at {self.timestamp}"
    




class VisitCount(models.Model):
    """
    The VisitCount model keeps track of the total number of visits and the timestamp of the last visit.
    Tracks the cumulative number of visits. PositiveIntegerField ensures only positive values are stored.
    default=0 initializes the count at zero when a VisitCount instance is created.
    Stores the timestamp of the most recent visit. 
    auto_now=True updates this field to the current timestamp every time the VisitCount instance is saved.
    """
    count = models.PositiveIntegerField(default=0)
    last_visit = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Total Visits: {self.count}"