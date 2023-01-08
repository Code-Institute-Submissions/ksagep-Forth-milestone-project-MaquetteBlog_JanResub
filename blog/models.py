"""Administrative tasks for build a model"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

"""Define the two variants of status"""
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """Describe the charactheristics of parts of post"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True
        )
    
    class Meta:
        """Define the descending order of the posts"""
        ordering = ['-created_on']

    def __str__(self):
        """Display the title of the post"""
        return self.title

    def number_of_likes(self):
        """Create likes counter"""
        return self.likes.count()

    def number_of_comments(self):
        """Create comments counter"""
        return self.comments.count()


class Comment(models.Model):
    """Describe the parts of comments"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        """Define the ascending order of the comments"""
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
