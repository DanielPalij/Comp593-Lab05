import requests

DEVELOPER_KEY = 'Y5m_pjuG-CQ1-PKjNuz7HCpfVJG4oQxv'
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'


def main():
    url = post_new_paste('This is a title', 'This\nis\nthe body', '1H', True )
    print(f'New paste URL: {url}')

def post_new_paste(title, body_text, expiration='10M', listed=False):
    """Posts a new public paste to PasteBin
    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): Expiration date of paste (N = Never, 10M = 10 Minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to '10M'.
        listed (bool, optional): Whether paste is publicly listed (True) or not (False). Defaults to False.
    Returns:
        str: URL of the new paste, if successful. None if unsuccessful.
    """
    # Setup the parameters for the request message
    paste_params = {
        'api_dev_key': DEVELOPER_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }
    
    # Send the post request to the PasteBin API
    print('Sending POST request to PasteBin API...', end='')
    resp_msg = requests.post(PASTEBIN_API_URL, data=paste_params)

    # Check whether the POST request was successful
    if resp_msg.ok:
        print('success')
        return resp_msg.text
    else:
        print('failed')
        print(f'Status code {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')

if __name__ == '__main__':
    main()