// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IoTDataStorage {
    struct PackageUpdate {
        uint256 timestamp;
        string city;
        string barangay;
        int256 latitude;
        int256 longitude;
        int256 temperatureCelsius;
        string status;
    }

    mapping(string => PackageUpdate[]) private packageHistory;
    string[] private packageIds;
    mapping(string => bool) private packageExists;

    address public owner;
    uint256 public constant MAX_ENTRIES = 100;

    event PackageUpdated(
        string packageId,
        uint256 timestamp,
        string city,
        string barangay,
        int256 latitude,
        int256 longitude,
        int256 temperatureCelsius,
        string status
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function storeUpdate(
        string memory packageId,
        string memory city,
        string memory barangay,
        int256 latitude,
        int256 longitude,
        int256 temperatureCelsius,
        string memory status
    ) public onlyOwner {
        require(packageHistory[packageId].length < MAX_ENTRIES, "Max entries reached for this package");

        if (!packageExists[packageId]) {
            packageIds.push(packageId);
            packageExists[packageId] = true;
        }

        packageHistory[packageId].push(PackageUpdate(
            block.timestamp,
            city,
            barangay,
            latitude,
            longitude,
            temperatureCelsius,
            status
        ));

        emit PackageUpdated(
            packageId,
            block.timestamp,
            city,
            barangay,
            latitude,
            longitude,
            temperatureCelsius,
            status
        );
    }

    function getLatestUpdate(string memory packageId) public view returns (
        uint256 timestamp,
        string memory city,
        string memory barangay,
        int256 latitude,
        int256 longitude,
        int256 temperatureCelsius,
        string memory status
    ) {
        require(packageHistory[packageId].length > 0, "No updates for this package");
        PackageUpdate memory update = packageHistory[packageId][packageHistory[packageId].length - 1];
        return (
            update.timestamp,
            update.city,
            update.barangay,
            update.latitude,
            update.longitude,
            update.temperatureCelsius,
            update.status
        );
    }

    function getUpdateByIndex(string memory packageId, uint256 index) public view returns (
        uint256 timestamp,
        string memory city,
        string memory barangay,
        int256 latitude,
        int256 longitude,
        int256 temperatureCelsius,
        string memory status
    ) {
        require(index < packageHistory[packageId].length, "Index out of bounds");
        PackageUpdate memory update = packageHistory[packageId][index];
        return (
            update.timestamp,
            update.city,
            update.barangay,
            update.latitude,
            update.longitude,
            update.temperatureCelsius,
            update.status
        );
    }

    function getUpdateCount(string memory packageId) public view returns (uint256) {
        return packageHistory[packageId].length;
    }

    function getAllPackageIds() public view returns (string[] memory) {
        return packageIds;
    }
}
