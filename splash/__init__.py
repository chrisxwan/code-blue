from passlib.apps import custom_app_context as pwd_context
import sendgrid
import os
from titlecase import titlecase

def hash_password(password):
    return pwd_context.encrypt(password)

def verify_password(password1, password2):
    return pwd_context.verify(password1, password2)

def sendVolunteerEmail(email):
    sg = sendgrid.SendGridClient(os.getenv('SENDGRID_USERNAME'), os.getenv('SENDGRID_PASSWORD'))
    message = sendgrid.Mail()
    spl = email.replace('@','.').split('.')
    firstname = titlecase(spl[0])
    lastname = titlecase(spl[1])
    message.add_to('%s %s <%s>' %(firstname, lastname, email))
    message.set_subject("""Help us run CodeBlue, YHack's high school learnathon""")
    message.set_html(buildVolunteerEmailHTMLEmail())
    message.set_text(buildVolunteerEmailTextEmail())
    message.set_from('YHack <team@yhack.org>')
    status,msg = sg.send(message)
    print "Volunteer Email To: %s, Status: %s" %(email, status)

def buildVolunteerEmailHTMLEmail():
    return """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>*|MC:SUBJECT|*</title>
            <style type="text/css">
                #outlook a{padding:0;}
                body{width:100% !important; background-color:#ffffff;-webkit-text-size-adjust:none; -ms-text-size-adjust:none;margin:0; padding:0;} 
                .ReadMsgBody{width:100%;} 
                .ExternalClass{width:100%;}
                ol li {margin-bottom:15px;}
                    
                img{height:auto; line-height:100%; outline:none; text-decoration:none;}
                #backgroundTable{height:100% !important; margin:0; padding:0; width:100% !important;}
                    
                p {margin: 1em 0;}
                    
                h1, h2, h3, h4, h5, h6 {color:#222222 !important; font-family:Arial, Helvetica, sans-serif; line-height: 100% !important;}
                    
                table td {border-collapse:collapse;}
                    
                .yshortcuts, .yshortcuts a, .yshortcuts a:link,.yshortcuts a:visited, .yshortcuts a:hover, .yshortcuts a span { color: black; text-decoration: none !important; border-bottom: none !important; background: none !important;}
                    
                .im {color:black;}
                div[id="tablewrap"] {
                        width:100%; 
                        max-width:600px!important;
                    }
                table[class="fulltable"], td[class="fulltd"] {
                        max-width:100% !important;
                        width:100% !important;
                        height:auto !important;
                    }
                            
                @media screen and (max-device-width: 430px), screen and (max-width: 430px) { 
                        td[class=emailcolsplit]{
                            width:100%!important; 
                            float:left!important;
                            padding-left:0!important;
                            max-width:430px !important;
                        }
                    td[class=emailcolsplit] img {
                    margin-bottom:20px !important;
                    }
                }
            </style>
        </head>
        <body style="width:100%; margin:0; padding:0; -webkit-text-size-adjust:none; -ms-text-size-adjust:none;">
        <table cellpadding="0" cellspacing="0" border="0" id="backgroundTable" style="height:auto !important; margin:0; padding:0; width:100% !important; color:#222222;">
            <tr>
                <td>
                <div id="tablewrap" style="width:90% !important; max-width:600px !important; text-align:center; margin:0 auto; padding-bottom:5px; padding-top:15px">
                      <table id="contenttable" width="600" align="center" cellpadding="0" cellspacing="0" border="0" style="background-color:#FFFFFF; margin:0 auto; text-align:center; border:none; width: 100% !important; max-width:600px !important;border-bottom-left-radius:5px;border-bottom-right-radius:5px">
                    <tr>
                        <td width="100%">
                            <table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="0" width="100%">
                                <tr>
                                    <td width="100%" bgcolor="#ffffff" style="text-align:center;"><a href="http://yhack.org"><img src="https://s3-us-west-2.amazonaws.com/yhack-static/header2.png" style="display:inline-block; max-width:100% !important; width:100% !important; height:auto !important;" border="0"></a>
                                    </td>
                                </tr>
                           </table>
                           <table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="25" width="100%">
                                <tr>
                                    <td width="100%" bgcolor="#ffffff" style="text-align:left;">
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:25px; padding:0; font-weight:normal;">
                                            Hi there!                        
                                        </p>
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            On Saturday, March 28th on Yale Campus, YHack is hosting CodeBlue, a one-day boot camp for high school students to learn about exciting topics in computer science, software engineering, entrepreneurship, and design through small workshops led by undergrad and graduate students.
                                        </p>
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            We are currently looking for three types of volunteers:
                                        </p>
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            <ol style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; font-weight:normal;">
                                                <li>General volunteers who will help run the logistics of the event.</li>
                                                <li>Mentors with HTML/CSS experience who will coach small groups of high school students in web development with a curriculum we have prepared.</li>
                                                <li>People who can teach a 30-40 minute elective about any relevant topics that interest them to high school students, such as artificial intelligence, graphic design, or mobile development.</li>
                                            </ol>
                                        </p>
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">                                    
                                            We are looking for undergrad and graduate students with all types of backgrounds to help out: you do not have to have programming experience to participate! 
                                        </p>

                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            If you are interested in volunteering or mentoring and would like to learn more, please fill out <a href="http://goo.gl/aBGb2l" target="_blank">this form</a> and visit us at <a href="http://codeblue.yhack.org" target="_blank">http://codeblue.yhack.org</a>. We will contact you at a closer date to the event to train you. In addition, if you know of any groups or individuals who would be interested, please forward this message to them.
                                        </p>

                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            We look forward to hearing from you!
                                        </p>
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            Best,
                                        </p>

                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            The YHack Team
                                        </p>

                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                            PS: if you help us out, you'll get free meals all day, t-shirts, and other swag
                                        </p>

                                        
                                     
                                    </td>
                                </tr>
                           </table>
                           <table bgcolor="#FFFFFF" border="0" cellspacing="0" width="100%" style="border-bottom-left-radius:5px;border-bottom-right-radius:5px;">
                                <tr>
                                    <td width="50%" bgcolor="#ffffff" style="text-align:left;border-bottom-left-radius:5px;border-bottom-right-radius:5px;padding-right:25px;padding-bottom:10px;padding-left:25px;">
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:11px; line-height:14px; margin-top:15px; margin-bottom:0px; padding:0; font-weight:normal;">
                                            Questions? Contact us at <a href="mailto:team@yhack.org">team@yhack.org</a>.<br>
                                        </p>
                                        <p style="color:#222222; font-family:Arial, Helvetica, sans-serif; font-size:11px; line-height:14px; margin-top:0px; margin-bottom:0px; padding:0; font-weight:normal;">
                                            Copyright 2015 YHack. All Rights Reserved.<br>
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                </div>
                </td>
            </tr>
        </table> 
        </body>
    </html>
    """

def buildVolunteerEmailTextEmail():
    return """
    Hi there!

    On Saturday, March 28th on Yale Campus, YHack is hosting CodeBlue, a one-day boot camp for high school\n
    students to learn about exciting topics in computer science, software engineering, entrepreneurship,\n
    and design through small workshops led by undergrad and graduate students.

    We are currently looking for three types of volunteers: 

    - General volunteers who will help run the logistics of the event.
    - Mentors with HTML/CSS experience who will coach small groups of high school students in web development\n
      with a curriculum we have prepared.
    - People who can teach a 30-40 minute elective about any relevant topics that interest them to high school\n
      students, such as artificial intelligence, graphic design, or mobile development.

    We are looking for undergrad and graduate students with all types of backgrounds to help out: you do not\n
    have to have programming experience to participate! 

    If you are interested in volunteering or mentoring and would like to learn more, please fill out this form:\n
    http://goo.gl/aBGb2l and visit us at http://codeblue.yhack.org. We will contact you at a closer date to the\n
    event to train you. In addition, if you know of any groups or individuals who would be interested, please\n
    forward this message to them.

    We look forward to hearing from you!

    Sincerely,
    The YHack Team

    PS: if you help us out, you'll get free meals all day, t-shirts, and other swag
    """