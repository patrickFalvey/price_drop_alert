class Price_Drop_Alert_CronJob(CronJobBase):
    '''
        Check Price_Alert table twice daily for price drops.
    '''
    RUN_AT_TIMES = ['06:00', '18:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'saasapp.views.Price_Drop_Alert_CronJob'

    def do(self):   
        if Price_Drop_Alert.objects.exist():
            alerts = Price_Drop_Alert.objects.all()
            for alert in alerts:
                product = Product.objects.filter(product_id=alert.item)
                if alert.price <= product.price:   
                    to_email = alert.email       
                    subject = '%s - %s' % (product.model, product.price) 
                    text_content = render_to_string('saas_app/email/price_drop_alert_email.txt', {'product': product})
                    html_content = render_to_string('saas_app/email/price_drop_alert_email.html', {'text_content': text_content, 'product': product})
                    msg = EmailMultiAlternatives(
                        subject,
                        text_content,
                        'noreply@ffldesign',
                        to_email)
                    msg.attach_alternative(html_content, 'text/html')
                    msg.mixed_subtype = 'related'
                    img_content_id = 'product'
                    img_data = open(product.image_url(), 'rb')
                    msg_img = MIMEImage(img_data.read())
                    img_data.close()
                    msg_img.add_header('Content-ID', '<{}>'.format(product.picture))
                    msg.attach(msg_img)
                    msg.send()
        else:
            pass
            
        
        
