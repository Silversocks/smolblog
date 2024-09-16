# smolblog
a simple, humble blog interface, for windows terminals

# built with
<p>Python</p>
<p>A little bit of csv, used in place of a proper DBMS</p>

# Getting Started
<p>Nothing too complicated here, just get the folder, execute the .py file, and you're good to go!</p>
<p>Please do ensure the files users.csv and the directory /Blog/are both present in the appropriate locations</p>

# User Manual
<p>The program opens with a display of a few of the posts inside it, and a terminal menu. The menu is based on text input, so the numbers corresponding to the action should be inputted to perform said action.</p> 
<p>If you aren't logged in already, the program presents a menu for dispplay, login, and signup. Choose the appropriate option as per your convenience, however, do remember that creating new posts and editing them are possible only if a user is logged in.</p>
<p>Signing up creates a new userid, and enables you to sign in with the same id in the future. Multiple users cannot share the same username</p>
<p>Once you log in, you can create new posts. You can also edit and delete your own posts. Editing other people's post, is considered rude in our socaity, and is thus, not a feature in this program. </p>


# Further Developmental Plans
<p>The program is built with a modular plan, to ensure new features can be added seamlessly. However, there are plans to improve it even further</p>
<p>The first goal involves replacing the simple csv file with a proper DBMS system, like MySql or Oracle, for better functionality</p>
<p>The second major goal is to change the ui from simple text input, to full interactive terminal/website interface. This can be achieved with pygame (for terminal) and django/flask (for website). </p>
<p>The third goal is to improve the utilisation of space, for a smoother user experience, and also faster processing of data.</p>
<p>The fourth goal is to add multiple layers of privileges, ie for the admin, moderator, verified users, and users.</p>
<p>The last goal is to implement a cookie system, or a session functionality, to keep users logged in even after they disconnect.</p>

# A Few Features...
<p>The program uses a csv file to store usernames and corrsponding passwords. The passwords are hashed, for security. The csv file is currently empty, but users can be added using the signup function in the menu</p>
<p>The posts are stored inside folders in the /Blog/ directory, which consists of subdirectories corresponding to each user, which in turn contains all their posts. A user cannot modify the contents of another user's directory</p>
<p>The programmer of this python file also happens to be an idiot, who forgot to add an exit button. You may need to resort to keyboardinterrupting your way out of this, if it comes down to it. </p>

# License
<p>lisences are cool</p>
