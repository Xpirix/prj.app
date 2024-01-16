## Setting up tailscale for SSH access

**Client side**

Follow the guide at https://tailscale.com/kb/installation to create an account and download Tailscale.

**Server side**

***Note: A sudo permission is required in order to install and run tailscale***

Install Tailscale by following the instructions at https://tailscale.com/kb/1031/install-linux or with the following command:

```
curl -fsSL https://tailscale.com/install.sh | sh
```

Start Tailscale with the following command:
```
sudo tailscale up
```
Paste the url provided by Tailscale in a browser and log in with the client account.

After logged in successfully, set up Tailscale SSH with the following command:

```
sudo tailscale set --ssh
```
The server machine should have the SSH tag in the Tailscale console. It's now accessible with SSH using a Terminal or the web browser through the Tailscale console.