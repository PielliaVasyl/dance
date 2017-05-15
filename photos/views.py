from django.shortcuts import render


def photos_show(request):
    title = 'Фото танца'

    # photos_directions = instances_groups(PhotoWikiAlbum)

    context = {
        'title': title,
        # 'photos_directions': photos_directions
    }
    return render(request, 'photos/photos.html', context)
