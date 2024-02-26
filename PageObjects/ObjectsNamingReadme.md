# How to name variables in Page Objects

## <span style="color:lightgreen">Locators</span>
<br>

1. Each variable is divided in two or three parts:
<ul>
    First Part: <b>[what type of element it is]</b>, Ex: input, button, href, img, svg, etc.
    <br>
    Second Part: <b>[what does the element do]</b>, Ex: email, submit, redirect, open, etc.
    <br>
    Third Part: <b>[where is the element located]</b>, Ex: login, contact_page, gallery, etc
</ul>
<table>
    <tr>
        <th>Type of Element</th>
        <th>Name of Element</th>
        <th>Location of Element</th>
        <th>Example</th>
        <th>Explanation</th>
    </tr>
    <tr>
        <td>btn (Button)</td>
        <td>login (Login Button)</td>
        <td>Login Page</td>
        <td>btn_log</td>
        <td>Represents a button in login page.</td>
    </tr>
    <tr>
        <td>tf (Text Field)</td>
        <td>username (Username)</td>
        <td>Login Page</td>
        <td>tf_usr</td>
        <td>Represents a text field of username.</td>
    </tr>
</table>

<br>

<hr style="border: 1px solid gray">

## <span style="color:cyan">Functions</span>
<br>

1. Each variable is divided in two or three parts:
<ul>
    First Part: <b>[action to perform]</b>, Ex: click, send, get, check, etc.
    <br>
    Second Part: <b>[performing action on what]</b>, Ex: email, submit, heading, textfield, etc.
    <br>
    Third Part: <b>[location]</b>, Ex: login, contact_page, frame, add_premise, etc
</ul>
<table>
    <tr>
        <th>Type of Action</th>
        <th>Action Performed on</th>
        <th>Location</th>
        <th>Example</th>
        <th>Explanation</th>
    </tr>
    <tr align="center">
        <td>clk (Click)</td>
        <td>btn (Button)</td>
        <td>Login Page</td>
        <td>clk_btn_log</td>
        <td>Click a button in login page.</td>
    </tr>
    <tr align="center">
        <td>get (Get)</td>
        <td>txt (Text Field)</td>
        <td>Contact Page</td>
        <td>get_txt_cont</td>
        <td>Get text from contact page.</td>
    </tr>
    <tr align="center">
        <td>send (Send)</td>
        <td>txt (Text Field)</td>
        <td>Add Premise</td>
        <td>send_txt_add</td>
        <td>Send text in add premise.</td>
    </tr>
</table>
