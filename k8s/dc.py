class Dc:
    def __init__(self,dc_template):
        self.name = dc_template.metadata.name if dc_template.metadata.name != None else "No name"
        self.image = [container.image for container in dc_template.spec.template.spec.containers]
        self.last_update, self.status_type = self._get_last_active_time(dc_template.status.conditions)

    def __str__(self):
        return "|| {0} || {1} || {2} || {3} ||".format(self.name,self.image,self.last_update,self.status_type)

    def _get_last_active_time(self,status_coditions_array):
        for i in status_coditions_array:
            if i.type == 'Available':
                return i.last_update_time.strftime("%Y-%m-%d-%H-%M-%S"),i.type
        return status_coditions_array[0].last_update_time.strftime("%m/%d/%Y - %H:%M:%S"), i.type