# Django-Image-API

- Upload images via HTTP request
- List of images

## Account tiers:

### The "Basic" plan after uploading an image get: 
- A link to a thumbnail that's 200px in height
### The "Premium" plan get:
- A link to a thumbnail that's 200px in height
- A link to a thumbnail that's 400px in height
- A link to the originally uploaded image
### The "Enterprise" plan get
- A link to a thumbnail that's 200px in height
- A link to a thumbnail that's 400px in height
- A link to the originally uploaded image
## Extra Features:
- Ability to fetch an expiring link to the image (the link expires after a given number of seconds (the user can specify any number between 300 and 30000))
- Create arbitrary tiers with the following things configurable:<br>
  - Abitrary thumbnail sizes<br>
  - Presence of the link to the originally uploaded file<br>
  - Ability to generate expiring links<br>
- Performance considerations (large image dataset and the API is frequently accessed)
