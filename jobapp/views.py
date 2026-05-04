from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Job, JobSeeker, JobAlert
from .forms import JobForm, JobSeekerForm
from .utils import haversine_distance


def home(request):
    return render(request, 'jobapp/home.html')


def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'jobapp/job_list.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobapp/job_detail.html', {'job': job})


def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobapp/post_job.html', {'form': form})


def subscribe_alert(request):
    if request.method == 'POST':
        form = JobSeekerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed for job alerts!')
            return redirect('job_list')
    else:
        form = JobSeekerForm()
    return render(request, 'jobapp/subscribe.html', {'form': form})


def nearby_jobs(request):
    jobs = []
    location_name = ''
    search_lat = None
    search_lon = None
    search_radius = 10

    if request.method == 'POST':
        location_name = request.POST.get('location_name', '')
        search_lat = request.POST.get('latitude')
        search_lon = request.POST.get('longitude')
        search_radius = int(request.POST.get('radius', 10))

        if search_lat and search_lon:
            search_lat = float(search_lat)
            search_lon = float(search_lon)
            all_jobs = Job.objects.filter(is_active=True)
            for job in all_jobs:
                dist = haversine_distance(search_lat, search_lon, job.latitude, job.longitude)
                if dist <= search_radius:
                    jobs.append((job, dist))
            jobs.sort(key=lambda x: x[1])

    return render(request, 'jobapp/nearby_jobs.html', {
        'jobs': jobs,
        'location_name': location_name,
        'search_lat': search_lat,
        'search_lon': search_lon,
        'search_radius': search_radius,
    })


def send_alerts(request):
    """
    Generate job alerts for nearby seekers.
    In a real system, this would be a management command or Celery task.
    """
    new_alerts = 0
    seekers = JobSeeker.objects.filter(is_active=True)
    jobs = Job.objects.filter(is_active=True)

    for seeker in seekers:
        for job in jobs:
            dist = haversine_distance(seeker.latitude, seeker.longitude, job.latitude, job.longitude)
            if dist <= seeker.radius_km:
                alert, created = JobAlert.objects.get_or_create(
                    job=job,
                    seeker=seeker,
                    defaults={'distance_km': dist}
                )
                if created:
                    new_alerts += 1

    messages.success(request, f'{new_alerts} new alerts generated!')
    return redirect('job_list')

