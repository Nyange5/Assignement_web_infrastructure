#!/bin/bash
# Unified firewall script for web-01, web-02, and lb-01

ROLE="$1"
LB_IP="172.20.0.10"

if [ -z "$ROLE" ]; then
    HOSTNAME=$(hostname)
    case "$HOSTNAME" in
        web-01|web-02) ROLE="web" ;;
        lb-01)         ROLE="lb" ;;
        *)
            echo "Could not detect role from hostname '$HOSTNAME'."
            echo "Run again with: ./firewall.sh web   OR   ./firewall.sh lb"
            exit 1
            ;;
    esac
fi

echo "Applying firewall rules for role: $ROLE (hostname: $(hostname))"

# --- Common base rules for all hosts ---
iptables -F
iptables -X
iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # SSH from anywhere, all hosts

# --- Role-specific rules ---
if [ "$ROLE" == "web" ]; then
    # HTTP (80) only from the load balancer
    iptables -A INPUT -p tcp --dport 80 -s "$LB_IP" -j ACCEPT
    echo "Web server rules applied: SSH (anywhere), HTTP (only from $LB_IP)"
elif [ "$ROLE" == "lb" ]; then
    # HTTPS (443) from anywhere
    iptables -A INPUT -p tcp --dport 443 -j ACCEPT
    echo "Load balancer rules applied: SSH (anywhere), HTTPS (anywhere)"
else
    echo "Unknown role: $ROLE. Use 'web' or 'lb'."
    exit 1
fi

echo ""
echo "Current rules:"
iptables -L -v -n
