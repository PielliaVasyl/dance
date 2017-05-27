from algoritms.entity_schedule import _get_filtered_instances
from entities.models import DanceStyleDirection


def instances_directions(entity, directions=None, direction_show=None, filters=None):
    if entity.objects.first():
        instances = entity.objects.all()
        if directions is None:
            directions = DanceStyleDirection.DIRECTIONS
        if direction_show is None:
            direction_show = DanceStyleDirection.DIRECTION_SHOW

        my_instances_directions = []
        for direction in directions:
            instances_for_particular_direction = instances.filter(dance_style__direction__title=direction)

            instances_for_particular_direction = _get_filtered_instances(instances_for_particular_direction, filters)

            if instances_for_particular_direction:
                instances_direction = {'direction': direction_show.get(direction, direction),
                                       'instances': instances_for_particular_direction}
                my_instances_directions.append(instances_direction)
        return my_instances_directions
    return []


def instances_groups(entity):
    groups = entity.objects.all()
    my_instances_groups = []
    for group in groups:
        instances_for_particular_group = group.get_instances_list()
        if instances_for_particular_group:
            instances_group = {'direction': {'title': group.title, 'link': group.link},
                               'instances': instances_for_particular_group}
            my_instances_groups.append(instances_group)
        return my_instances_groups
    return []
