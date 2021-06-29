**PhotoShare-api**

**PhotoShare-api** - An api for a simple PhotoSharing Application

## User Stories

### PROFILES
- [x] An authenticated User can retrieve a list of profiles on the platform by sending a GET request to /api/profiles/. Each profile object contains the following fields (including a url to access that specific profile)
- ![1 profile1](https://user-images.githubusercontent.com/32243848/114430307-4dec7180-9b8c-11eb-9abc-c780db08cbdf.gif)

- [x] An authenticated User can retrieve a profile object by sending a GET request to /api/profiles/\<int:profile_id> containing the following fields
- ![2 profile2](https://user-images.githubusercontent.com/32243848/114430312-4fb63500-9b8c-11eb-83c9-f53202cf0a5f.gif)

- [x] An authenticated User can edit her bio (PUT/PATCH) at /api/profile/\<int:profile_id> but **NOT** the bio of others. The request should return the following fields
- ![3 profile3 0](https://user-images.githubusercontent.com/32243848/114430320-50e76200-9b8c-11eb-9c73-f5af39784e8d.gif)
- ![4 profile3 1](https://user-images.githubusercontent.com/32243848/114430328-52188f00-9b8c-11eb-85f2-8966e5c644ad.gif)

### POSTS
- [x] An authenticated User can retrieve a list of posts by sending a GET request to /api/posts/. Each post object contains the following fields (including a url to access that specific post)
- ![5 posts1](https://user-images.githubusercontent.com/32243848/114430447-6e1c3080-9b8c-11eb-8176-129841a2e1b0.gif)

- [x] An authenticated User can add a new post by sending a POST request to /api/posts. Only a description is required, the imageField should be set to blank. The added post should automatically be associated with the user who submitted the request. The request should return the following fields
- ![6 posts2](https://user-images.githubusercontent.com/32243848/114430456-6fe5f400-9b8c-11eb-9b95-69d2fa21588c.gif)

- [x] An authenticated User can change any of her posts' description by sending a PUT/PATCH request to /api/posts/\<int:post_id> but **NOT** the posts of others.
- ![7 posts3](https://user-images.githubusercontent.com/32243848/114430463-72484e00-9b8c-11eb-899e-5dc33a1cc385.gif)
- ![8 posts4 0](https://user-images.githubusercontent.com/32243848/114435336-0bc62e80-9b92-11eb-9843-264613462417.gif)

- [x] An authenticated User can delete any of her posts by sending a DELETE request to /api/posts/\<int:post_id> but **NOT** the posts of others. the request should return an HTTP 204 No Content
- ![8 posts4 1](https://user-images.githubusercontent.com/32243848/114435340-0d8ff200-9b92-11eb-83d2-22e65e91c827.gif)
- ![8 posts4 2](https://user-images.githubusercontent.com/32243848/114435351-0ff24c00-9b92-11eb-9c27-0ef3a185f0c6.gif)
- ![8 posts4 3](https://user-images.githubusercontent.com/32243848/114435355-11237900-9b92-11eb-8f55-0829e565336f.gif)

### COMMENTS
- [x] An authenticated User can retrieve a list of comments on a post by sending a GET request to /api/posts/\<int:post_id>/comments/. Each post object contains the following fields
- ![9 comments1](https://user-images.githubusercontent.com/32243848/114437264-50eb6000-9b94-11eb-8fa0-97b67b8bec56.gif)

- [x] An authenticated User can add a new comment to a post by sending a POST request to /api/posts/\<int:post_id>/comments/. The added comment should automatically be
associated with the user who submitted the request. The request should return the new list of comments OR the specific comment that was added
- ![10 comments2](https://user-images.githubusercontent.com/32243848/114437270-521c8d00-9b94-11eb-9f6a-3fca8873a753.gif)

### MISC
- [x] All endpoints require some form of authentication (i.e unathenticated clients cannot access endpoints)
- ![11 misc1](https://user-images.githubusercontent.com/32243848/114437845-0dddbc80-9b95-11eb-9ede-e9939a8985c3.gif)

- [x] A user should able to access a Browsable version (with login) of the API in Browser
- ![12 optional1](https://user-images.githubusercontent.com/32243848/114441081-edaffc80-9b98-11eb-8828-51f1a1e01cc1.gif)

- [x] An authenticated User can edit any of her comments on a post by sending a POST request to /api/posts/\<int:post_id>/comments/\<int:comment_id> but **NOT** the comments of others.
- ![13 optional2](https://user-images.githubusercontent.com/32243848/114441082-ee489300-9b98-11eb-851d-6ec82d801940.gif)
- ![14 optional3](https://user-images.githubusercontent.com/32243848/114441086-ef79c000-9b98-11eb-9214-dddf9dbfd1d2.gif)

- [x] An authenticated User can delete any of her comments on a post by sending a DELETE request to /api/posts/\<int:post_id>/comments/\<int:comment_id>/ but **NOT** the comments of others.
- ![15 optional4](https://user-images.githubusercontent.com/32243848/114441093-f1438380-9b98-11eb-9f1e-cd334c3c0764.gif)
- ![16 optional5](https://user-images.githubusercontent.com/32243848/114441099-f30d4700-9b98-11eb-96fd-6023001efa91.gif)

## License

    Copyright [2021] [Kazi Siam]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
